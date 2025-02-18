import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerPercentB_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerPercentB und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'BollingerPercentB': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
