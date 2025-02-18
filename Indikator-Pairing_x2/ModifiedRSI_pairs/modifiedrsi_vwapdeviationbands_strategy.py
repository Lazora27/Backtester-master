import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
