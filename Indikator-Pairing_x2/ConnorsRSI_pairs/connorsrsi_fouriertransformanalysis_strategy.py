import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
