import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketFacilitationIndex_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketFacilitationIndex und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'MarketFacilitationIndex': 1.0,
            'HilbertSinewave': 1.0
        })
    )
