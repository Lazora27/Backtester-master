import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandWidth_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandWidth und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'BollingerBandWidth': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
