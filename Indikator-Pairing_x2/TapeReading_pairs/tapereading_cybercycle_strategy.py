import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und CyberCycle
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'CyberCycle': 1.0
        })
    )
