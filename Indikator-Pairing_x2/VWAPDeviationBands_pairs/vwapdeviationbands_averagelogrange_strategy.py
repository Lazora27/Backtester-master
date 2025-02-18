import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'AverageLogRange': 1.0
        })
    )
