import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_MarketFacilitationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und MarketFacilitationIndex
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'MarketFacilitationIndex': 1.0
        })
    )
