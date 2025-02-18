import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
