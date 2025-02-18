import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HyperbolicVolatility_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HyperbolicVolatility und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'HyperbolicVolatility': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
