import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketFacilitationIndex_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketFacilitationIndex und TrendCycles
    """
    
    params = (
        ('indicators', {
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'MarketFacilitationIndex': 1.0,
            'TrendCycles': 1.0
        })
    )
