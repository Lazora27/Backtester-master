import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolatilityIndex_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolatilityIndex und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'VolatilityIndex': 1.0,
            'AverageTrueRange': 1.0
        })
    )
