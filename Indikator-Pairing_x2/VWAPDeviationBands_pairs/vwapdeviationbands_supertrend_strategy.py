import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und SuperTrend
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'SuperTrend': 1.0
        })
    )
