import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
