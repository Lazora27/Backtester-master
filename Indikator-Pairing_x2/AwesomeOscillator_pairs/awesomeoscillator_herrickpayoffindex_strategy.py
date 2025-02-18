import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_HerrickPayoffIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und HerrickPayoffIndex
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'HerrickPayoffIndex': 1.0
        })
    )
