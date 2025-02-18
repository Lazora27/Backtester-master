import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandSqueeze_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandSqueeze und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'BollingerBandSqueeze': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
