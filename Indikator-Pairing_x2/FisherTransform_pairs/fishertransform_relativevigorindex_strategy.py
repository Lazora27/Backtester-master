import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_RelativeVigorIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und RelativeVigorIndex
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'RelativeVigorIndex': 1.0
        })
    )
