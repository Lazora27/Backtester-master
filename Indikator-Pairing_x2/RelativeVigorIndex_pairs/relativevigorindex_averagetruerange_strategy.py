import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'AverageTrueRange': 1.0
        })
    )
