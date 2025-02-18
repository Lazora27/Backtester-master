import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'AverageTrueRange': 1.0
        })
    )
