import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DynamicMomentumIndex_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DynamicMomentumIndex und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'DynamicMomentumIndex': 1.0,
            'AverageTrueRange': 1.0
        })
    )
