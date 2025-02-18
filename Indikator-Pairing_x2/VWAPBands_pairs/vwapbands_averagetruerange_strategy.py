import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'AverageTrueRange': 1.0
        })
    )
