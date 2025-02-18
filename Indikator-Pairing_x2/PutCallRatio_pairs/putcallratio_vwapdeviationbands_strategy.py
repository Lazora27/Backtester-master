import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
