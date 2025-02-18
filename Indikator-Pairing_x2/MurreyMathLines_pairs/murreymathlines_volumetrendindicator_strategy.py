import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_VolumeTrendIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und VolumeTrendIndicator
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'VolumeTrendIndicator': 1.0
        })
    )
