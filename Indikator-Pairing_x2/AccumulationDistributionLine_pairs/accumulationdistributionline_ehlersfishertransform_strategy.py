import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccumulationDistributionLine_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccumulationDistributionLine und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'AccumulationDistributionLine': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
