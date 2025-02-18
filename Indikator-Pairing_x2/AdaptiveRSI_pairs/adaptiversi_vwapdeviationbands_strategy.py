import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
