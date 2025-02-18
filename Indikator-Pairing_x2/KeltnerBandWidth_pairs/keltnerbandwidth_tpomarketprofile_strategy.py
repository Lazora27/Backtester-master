import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerBandWidth_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerBandWidth und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'KeltnerBandWidth': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
