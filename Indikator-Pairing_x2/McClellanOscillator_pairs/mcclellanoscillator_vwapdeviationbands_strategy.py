import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
