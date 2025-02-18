import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'AverageTrueRange': 1.0
        })
    )
