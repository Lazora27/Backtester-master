import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
