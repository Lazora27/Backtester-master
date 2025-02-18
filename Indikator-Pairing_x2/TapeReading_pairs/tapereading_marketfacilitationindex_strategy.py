import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_MarketFacilitationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und MarketFacilitationIndex
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'MarketFacilitationIndex': 1.0
        })
    )
