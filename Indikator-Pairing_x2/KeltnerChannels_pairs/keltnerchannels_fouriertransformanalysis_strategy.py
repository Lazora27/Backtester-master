import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
