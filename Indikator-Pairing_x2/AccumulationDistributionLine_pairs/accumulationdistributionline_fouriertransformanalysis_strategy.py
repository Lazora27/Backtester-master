import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccumulationDistributionLine_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccumulationDistributionLine und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'AccumulationDistributionLine': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
