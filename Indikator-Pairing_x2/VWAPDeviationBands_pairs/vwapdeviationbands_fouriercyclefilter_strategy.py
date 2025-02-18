import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
