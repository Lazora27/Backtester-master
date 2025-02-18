import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_RelativeStrengthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und RelativeStrengthIndex
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'RelativeStrengthIndex': 1.0
        })
    )
