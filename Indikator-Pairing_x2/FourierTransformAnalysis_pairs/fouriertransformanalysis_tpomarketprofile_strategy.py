import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FourierTransformAnalysis_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FourierTransformAnalysis und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'FourierTransformAnalysis': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
