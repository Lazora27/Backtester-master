import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_KaufmanEfficiencyRatio_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und KaufmanEfficiencyRatio
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'KaufmanEfficiencyRatio': {
                'class': KaufmanEfficiencyRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KaufmanEfficiencyRatio'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'KaufmanEfficiencyRatio': 1.0
        })
    )
