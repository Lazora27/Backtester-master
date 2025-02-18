import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und CyberCycle
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'CyberCycle': 1.0
        })
    )
