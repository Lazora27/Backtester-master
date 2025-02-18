import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'AdaptiveATR': 1.0
        })
    )
