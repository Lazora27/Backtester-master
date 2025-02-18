import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
