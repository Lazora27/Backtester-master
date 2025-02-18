import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
