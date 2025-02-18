import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketFacilitationIndex_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketFacilitationIndex und CycleFinder
    """
    
    params = (
        ('indicators', {
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'MarketFacilitationIndex': 1.0,
            'CycleFinder': 1.0
        })
    )
