import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BradleySiderograph_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BradleySiderograph und CyberCycle
    """
    
    params = (
        ('indicators', {
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'BradleySiderograph': 1.0,
            'CyberCycle': 1.0
        })
    )
