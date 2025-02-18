import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und CyberCycle
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'CyberCycle': 1.0
        })
    )
