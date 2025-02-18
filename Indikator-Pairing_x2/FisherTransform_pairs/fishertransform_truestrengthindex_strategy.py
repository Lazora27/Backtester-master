import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_TrueStrengthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und TrueStrengthIndex
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'TrueStrengthIndex': 1.0
        })
    )
