import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BradleySiderograph_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BradleySiderograph und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'BradleySiderograph': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
