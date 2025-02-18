import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_VolumeFlowIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und VolumeFlowIndicator
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'VolumeFlowIndicator': 1.0
        })
    )
