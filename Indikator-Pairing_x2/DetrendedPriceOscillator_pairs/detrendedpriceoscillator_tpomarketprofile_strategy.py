import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DetrendedPriceOscillator_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DetrendedPriceOscillator und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'DetrendedPriceOscillator': {
                'class': DetrendedPriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DetrendedPriceOscillator1'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'DetrendedPriceOscillator': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
