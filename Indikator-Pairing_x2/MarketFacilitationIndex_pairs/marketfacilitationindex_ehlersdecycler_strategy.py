import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketFacilitationIndex_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketFacilitationIndex und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'MarketFacilitationIndex': 1.0,
            'EhlersDecycler': 1.0
        })
    )
