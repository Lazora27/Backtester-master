import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AroonIndicator_MarketFacilitationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AroonIndicator und MarketFacilitationIndex
    """
    
    params = (
        ('indicators', {
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            },
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            }
        }),
        ('weights', {
            'AroonIndicator': 1.0,
            'MarketFacilitationIndex': 1.0
        })
    )
