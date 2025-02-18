import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'AccelerationBands': 1.0
        })
    )
