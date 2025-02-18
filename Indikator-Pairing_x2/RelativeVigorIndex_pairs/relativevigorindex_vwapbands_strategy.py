import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und VWAPBands
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'VWAPBands': 1.0
        })
    )
