import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandWidth_MarketFacilitationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandWidth und MarketFacilitationIndex
    """
    
    params = (
        ('indicators', {
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            },
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            }
        }),
        ('weights', {
            'BollingerBandWidth': 1.0,
            'MarketFacilitationIndex': 1.0
        })
    )
