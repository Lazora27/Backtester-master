import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_TapeReading_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und TapeReading
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'TapeReading': 1.0
        })
    )
