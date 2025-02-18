import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'AverageTrueRange': 1.0
        })
    )
