import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und GannAngles
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'GannAngles': 1.0
        })
    )
